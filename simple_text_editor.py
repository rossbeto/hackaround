# https://www.hackerrank.com/challenges/simple-text-editor/problem?isFullScreen=true
#testcase 7,8,9,10,11 TIMEOUT

from enum import Enum


class OperationType(Enum):
    APPEND = 1
    DELETE = 2
    PRINT = 3
    UNDO = 4


class Statement:
    def __init__(self, operation_type, arg, part=None):
        self.operation_type = operation_type
        self.arg = arg
        self.part = part

# SimpleTextEditorOperation is the class to read and then decide whether it is the time to start some operation on SimpleTextEditor
# if the statement is print( which will affect the result), then it is the time to execute all the operations that has been read so far ( but not yet executed)
# mean that if the input are just append, delete ... without printing -> the execution will be delayed until a PRINT is read

# SimpleTextEditor will hold all mutatable statement ( append and delete) that has been executed
# print and undo will be execute without storing the statement in editor queue
# for undo, just need to take the last statement in the editor queue (either append or delete) and then perform undo
class SimpleTextEditor:
    def __init__(self):
        self._text = ''
        self.statements = list()
    
    def append(self, w):
        # self._text = f'{self._text}{w}'
        self._text = ''.join([self._text, w])
        stm_append = Statement(OperationType.APPEND, w)
        self.statements.append(stm_append)
        # print(f'append:{self._text}')
    
    def delete(self, k):
        k = int(k)
        # l = len(self._text)
        # number_of_char_to_be_removed = min(l, k)
        number_of_char_to_be_removed = k
        # part = self._text[l-number_of_char_to_be_removed:l]
        part = self._text[-number_of_char_to_be_removed:]
        # self._text = self._text[0:l-number_of_char_to_be_removed]
        self._text = self._text[:-number_of_char_to_be_removed]

        stm_delete = Statement(OperationType.DELETE, k, part)
        self.statements.append(stm_delete)
        
        # print(f'delete:{self._text}')
    
    def print(self, k):
        k = int(k)
        print(self._text[k-1])
        # byright, should check len(), but if testcase are correct, then no need to check (save some calculation)
        # if k <= len(self._text) and k >0:
        #     print(self._text[k-1])
        # print(f'print:{self._text}')
    
    def _undo_append(self, stm_append):
        _w = stm_append.arg
        l_w = len(_w)
        # l = len(self._text)
        self._text = self._text[:-l_w]
    
    def _undo_delete(self, stm_delete):
        part = stm_delete.part
        self._text += part
    
    def remove_stm(self):
        # print(f'remove_stm.{self.statements}')
        stm = self.statements.pop()
        return stm
    
    def undo(self):
        stm = self.remove_stm()
        if stm.operation_type == OperationType.APPEND:
            self._undo_append(stm)
        elif stm.operation_type == OperationType.DELETE:
            self._undo_delete(stm)
        
        # print(f'undo:{self._text}')


class SimpleTextEditorOperation:
    def __init__(self):
        self.text_editor = SimpleTextEditor()
        self.operations = list()
        self.number_of_chars = 0
    
    def perform_operation(self, operation_type, arg):
        # print('perform_operation')
        if operation_type == OperationType.APPEND:
            self.text_editor.append(arg)
        elif operation_type == OperationType.DELETE:
            self.text_editor.delete(arg)
        elif operation_type == OperationType.PRINT:
            self.text_editor.print(arg)
        elif operation_type == OperationType.UNDO:
            self.text_editor.undo()
    
    def add_operation(self, stm):
        # print('add_operation')
        self.operations.append({
            'stm': stm,
            'done': False
        })
        # if stm.operation_type == OperationType.APPEND:
        #     self.number_of_chars += len(stm.arg)
        # elif stm.operation_type == OperationType.DELETE:
        #     self.number_of_chars -= int(stm.arg)
        
        # if self.number_of_chars < 0:
        #     self.number_of_chars = 0
    
    def check_and_execute(self):
        last_operation = self.operations[-1]
        last_stm = last_operation['stm']
        if last_stm.operation_type == OperationType.PRINT:
            # print('now printing')
            for op in self.operations:
                if not op['done']:
                    stm = op['stm']
                    self.perform_operation(stm.operation_type, stm.arg)
                    op['done'] =  True
            # now remove PRINT
            # self.operations.pop()

            # now empty the operations list - start again
            # if we empty the list here, then for UNDO -> need to cater for self.operations empty
            # clear the list here -> better for performance (testcase 12,13,14 passed - while "remove only PRINT and keep self.operations list" makes those testcases failed)
            self.operations = list()
        elif last_stm.operation_type == OperationType.UNDO:
            # this is UNDO statement
            self.operations.pop()
            l_o = len(self.operations) 

            # this is when we empty self.operations in PRINT self.operations = list()
            if l_o > 0:
                prev_op = self.operations.pop()
            elif l_o == 0:
                self.perform_operation(last_stm.operation_type, last_stm.arg)


            # if len(self.operations) > 0:
            #     prev_op = self.operations.pop()
            #     # if all previous Operations are done, now we need to do UNDO
            #     if prev_op['done']:
            #         self.perform_operation(last_stm.operation_type, last_stm.arg)
            #     else:
            #         # remove the last operation, since we can just take advantage of this UNDO and remove that prev Operation( which has not been executed)
            #         pass
        
        # this APPROACH is wrong, since DELETE cannot be used to remove previous APPEND -> because if another UNDO come next, it will just remove this DELETE ( and the previous APPEND is supposed to be effective)
        # elif last_stm == Operation.DELETE:
        #     # if there is a DELETE(minus) - try to adjust the current Operations stack
        #     i = len(self.operations)
        #     number_of_chars_to_remove = int(last_stm.arg)
        #     while number_of_chars_to_remove > 0 and i>0:
        #         i -= 1
        #         op = self.operations[i]
        #         stm = op['stm']
        #         if stm.operation_type == Operation.APPEND and not op['done']:
        #             # number of charecter of APPEND to be added
        #             n = len(stm.arg)
        #             number_of_chars_to_remove -= n
        #             # if number_of_chars_to_remove > this APPEND -> mark APPEND as DONE, and reduce number_of_chars_to_remove
        #             if number_of_chars_to_remove >= 0:
        #                 op['done'] = True
        #             else:
        #             # if number_of_chars_to_remove < this APPEND -> adjust APPEND(stm)
        #                 stm.arg = stm.arg[:-number_of_chars_to_remove]

        #     if number_of_chars_to_remove >= 0:
        #         last_stm.arg = number_of_chars_to_remove
        #     else:

        #     pass

def read_input(input_file_path):
    input_file = open(input_file_path, "r")
    n = int(input_file.readline().rstrip())
    text_operation = SimpleTextEditorOperation()
    for i in range(n):
        line = input_file.readline()
        stms = line.rstrip().split()
        operation_type = OperationType(int(stms[0]))
        arg = None
        if operation_type != OperationType.UNDO:
            arg = stms[1]

        stm = Statement(operation_type, arg)
        text_operation.add_operation(stm)
        text_operation.check_and_execute()


def main():
    print('Sample 1')
    read_input('.\data\simple_text_editor_ip1.txt')
    print('\nSample 2')
    read_input('.\data\simple_text_editor_ip2.txt')


if __name__ == "__main__":
    main()

