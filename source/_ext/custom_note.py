from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
from mytrans import mytranslate

class customNote(nodes.Admonition, nodes.Element):
    pass

def visit_todo_node(self, node):
    self.visit_admonition(node)
    self.body[-1] = self.body[-1].replace("admonition", "admonition "+node.pclass)

def depart_todo_node(self, node):
    self.depart_admonition(node)

class CustomNoteDirective(SphinxDirective):
    # this enables content in the directive
    has_content = True
    def run(self):
        targetid = self.pclass+'-note-%d' % self.env.new_serialno(self.pclass)
        targetnode = nodes.target('', '', ids=[targetid], classes=[self.pclass])
        todo_node = self.pobject('\n'.join(self.content))
        todo_node += nodes.title(mytranslate(self.pname), mytranslate(self.pname))
        self.state.nested_parse(self.content, self.content_offset, todo_node)
        if not hasattr(self.env, 'custom_all_customs'):
            self.env.custom_all_customs = []
        self.env.custom_all_customs.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'todo': todo_node.deepcopy(),
            'target': targetnode,
            'class': self.pclass,
        })
        return [targetnode, todo_node]

def purge_todos(app, env, docname):
    if not hasattr(env, 'language'):
        env.language = app.config.language
    if not hasattr(env, 'custom_all_customs'):
        return
    env.custom_all_customs = [todo for todo in env.custom_all_customs
                          if todo['docname'] != docname]

def merge_todos(app, env, docnames, other):
    if not hasattr(env, 'custom_all_customs'):
        env.custom_all_customs = []
    if hasattr(other, 'custom_all_customs'):
        env.custom_all_customs.extend(other.custom_all_customs)
    if not hasattr(env, 'language'):
        env.language = app.config.language

def process_todo_nodes(app, doctree, fromdocname):
    #if not app.config.todo_include_todos:
    #    for node in doctree.traverse(todo):
    #        node.parent.remove(node)
    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env
    if not hasattr(env, 'custom_all_customs'):
        env.custom_all_customs = []
    if not hasattr(env, 'language'):
        env.language = app.config.language



class observationNote(customNote):
    pname = 'Osservazione'
    pclass = "observation"

class ObservationNoteDirective(CustomNoteDirective):
    pname = 'Osservazione'
    pclass = "observation"
    pobject = observationNote


class questionNote(customNote):
    pname = 'Domanda'
    pclass = "question"

class questionNoteDirective(CustomNoteDirective):
    pname = 'Domanda'
    pclass = "question"
    pobject = questionNote

def setup(app):
    #app.add_config_value('todo_include_todos', False, 'html')
    app.add_node(observationNote,
            html=(visit_todo_node, depart_todo_node),
            latex=(visit_todo_node, depart_todo_node),
            text=(visit_todo_node, depart_todo_node))
    app.add_node(questionNote,
            html=(visit_todo_node, depart_todo_node),
            latex=(visit_todo_node, depart_todo_node),
            text=(visit_todo_node, depart_todo_node))
    app.add_directive('observation_note', ObservationNoteDirective)
    app.add_directive('question_note', questionNoteDirective)
    app.connect('doctree-resolved', process_todo_nodes)
    app.connect('env-purge-doc', purge_todos)
    app.connect('env-merge-info', merge_todos)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }