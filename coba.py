from automata.fa.dfa import DFA

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

print(dfa.accepts_input('1010'))
print(dfa.accepts_input('100')) 
print(dfa.accepts_input('10'))    
print(dfa.accepts_input('1000'))  
print(dfa.accepts_input('1100'))
