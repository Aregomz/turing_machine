class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convierte la cadena de entrada en una lista
        self.head = 0  # Posición inicial de la cabeza
        self.state = 'q0'  # Estado inicial

    def get_tape(self):
        return ''.join(self.tape)  # Devuelve el contenido del tape como una cadena

    def is_accepted(self):
        return self.state == 'q_accept'  # Comprueba si el estado es de aceptación

    def run(self):
        while self.state != 'q_accept' and self.state != 'q_reject':
            current_symbol = self.tape[self.head]

            if self.state == 'q0':
                if current_symbol == '0':
                    self.tape[self.head] = 'X'  # Reemplaza 0 con X
                    self.head += 1  # Mueve la cabeza a la derecha
                    self.state = 'q1'  # Cambia a q1
                elif current_symbol == 'Y' or current_symbol == 'X':
                    self.head += 1  # Mueve la cabeza a la derecha
                elif current_symbol == ' ':
                    self.state = 'q_accept'  # Si llega al espacio, acepta

            elif self.state == 'q1':
                if current_symbol == '1':
                    self.tape[self.head] = 'Y'  # Reemplaza 1 con Y
                    self.head -= 1  # Mueve la cabeza a la izquierda
                    self.state = 'q2'  # Cambia a q2
                elif current_symbol == '0':
                    self.head += 1  # Mueve la cabeza a la derecha
                elif current_symbol == 'Y':
                    self.head += 1  # Mueve la cabeza a la derecha
                elif current_symbol == ' ':
                    self.state = 'q_reject'  # Si llega al espacio sin haber procesado, rechaza

            elif self.state == 'q2':
                if current_symbol == 'X':
                    self.head += 1  # Mueve la cabeza a la derecha
                    self.state = 'q0'  # Vuelve al estado q0
                elif current_symbol == 'Y':
                    self.head += 1  # Mueve la cabeza a la derecha
                elif current_symbol == ' ':
                    self.state = 'q_accept'  # Si llega al espacio, acepta

        # Si se sale sin aceptación, pasa al estado de rechazo
        if self.state != 'q_accept':
            self.state = 'q_reject'
