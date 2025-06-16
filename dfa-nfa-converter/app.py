from flask import Flask, render_template, request
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

app = Flask(__name__)

# DFA: Menerima jumlah 0 genap
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)

nfa = NFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}, '1': {'q0'}},
        'q1': {'0': {'q0'}, '1': {'q1'}}
    },
    initial_state='q0',
    final_states={'q0'}
)

def convert_to_binary(value, base):
    if base == 'decimal':
        return bin(int(value))[2:]
    elif base == 'octal':
        return bin(int(value, 8))[2:]
    elif base == 'hex':
        return bin(int(value, 16))[2:]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'clear':
            return render_template('index.html', binary_value='', result='', steps=[], machine='dfa', mermaid_code='', dfa_final_states=dfa.final_states, final_state='')

        value = request.form['value']
        base = request.form['base']
        machine = request.form['machine']

        binary_value = convert_to_binary(value, base)
        steps = []
        result = ''
        mermaid_code = ""
        final_state = ""

        if machine == 'dfa':
            accepted = dfa.accepts_input(binary_value)
            result = "Accepted" if accepted else "Rejected"
            state = dfa.initial_state
            mermaid_code = "stateDiagram-v2\n"
            mermaid_code += f"[*] --> {dfa.initial_state}\n"

            for char in binary_value:
                next_state = dfa.transitions[state][char]
                steps.append((state, char, next_state))
                mermaid_code += f"{state} --> {next_state}: \"{char}\"\n"
                state = next_state

            final_state = state
            mermaid_code += f"{final_state} --> [*]\n"
            for fs in dfa.final_states:
                mermaid_code += f"state {fs} <<final>>\n"

        else:  # NFA
            accepted = nfa.accepts_input(binary_value)
            result = "Accepted" if accepted else "Rejected"
            steps = [("NFA tidak memiliki transisi deterministik seperti DFA", "", "")]
            mermaid_code = "stateDiagram-v2\n    note right of q0: NFA tidak divisualisasi otomatis\n"
            final_state = "N/A"

        return render_template('index.html',
                                binary_value=binary_value,
                                result=result,
                                steps=steps,
                                machine=machine,
                                mermaid_code=mermaid_code,
                                dfa_final_states=list(dfa.final_states),
                                final_state=final_state)

    return render_template('index.html', binary_value='', result='', steps=[], machine='dfa', mermaid_code='', dfa_final_states=dfa.final_states, final_state='')

if __name__ == '__main__':
    app.run(debug=True)
