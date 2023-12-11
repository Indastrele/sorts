import random
import time


class Array:
    def __init__(self):
        self.__array = list()
        self.__sort_time = float()

    # generate method for int and str
    def __generator(self, left_border, right_border, size):
        for i in range(0, size):
            self.__array.append(random.randint(left_border, right_border))

    def __float_generator(self, left_border, right_border, size):
        for i in range(0, size):
            self.__array.append(round(random.uniform(left_border, right_border), 3))

    # method for generating array with some preferences
    def generate(self, left, right, size_input):
        self.__array = list()
        # check input in all line edits in program
        if len(left) == 0 or len(right) == 0 or len(size_input) == 0:
            return "Сообщение об ошибке", "Отсутствует ввод данных"
        # check size input to be an integer
        if size_input.isdigit():
            size = int(size_input)
        else:
            return"Сообщение об ошибке", "Размер должен быть целым числом"

        # check borders input to be char
        if left.isalpha() and right.isalpha():
            if len(left) > 1 or len(right) > 1:
                return "Error", "Input is string, not char."

            left = ord(left)
            right = ord(right)

            if right < left:
                return "Сообщение об ошибке", "Некорректный ввод данных"

            self.__generator(left, right, size)
            tmp_array = list()
            for i in self.__array:
                tmp_array.append(chr(i))

            self.__array = tmp_array
        elif (left.isdigit() or left[0] == "-" and left[1:].isdigit())\
                and (right.isdigit() or right[0] == "-" and right[1:].isdigit()):
            left = int(left)
            right = int(right)

            if right < left:
                return "Сообщение об ошибке", "Некорректный ввод данных"

            self.__generator(left, right, size)
        elif not left.isalpha() and not right.isalpha() and ("." in left or "." in right):
            if not str(left[::left.find('.')] + left[left.find('.')::]).isdigit() or not str(right[::right.find('.')] + right[right.find('.')::]).isdigit() :
                return "Сообщение об ошибке", "Некорректный ввод данных"
            left = float(left)
            right = float(right)

            if right < left:
                return "Сообщение об ошибке", "Некорректный ввод данных"

            self.__float_generator(left, right, size)
        else:
            return "Сообщение об ошибке", "Данные должны быть одного типа"
        return 'Ok'

    def __merge_sort_nums_ascending(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)

        self.__merge_sort_nums_ascending(left, mid)
        self.__merge_sort_nums_ascending(mid + 1, right)

        i = left
        j = mid + 1
        tmp = list()
        for step in range(0, right - left + 1):
            if j > right or (i < mid + 1 and self.__array[i] < self.__array[j]):
                tmp.append(self.__array[i])
                i += 1
            else:
                tmp.append(self.__array[j])
                j += 1

        for step in range(0, right - left + 1):
            if self.__array[left + step] != tmp[step]:
                self.__array[left + step] = tmp[step]

    def __merge_sort_strings_ascending(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)

        self.__merge_sort_strings_ascending(left, mid)
        self.__merge_sort_strings_ascending(mid + 1, right)

        i = left
        j = mid + 1
        tmp = list()
        for step in range(0, right - left + 1):
            if j > right or (i < mid + 1 and self.__array[i].lower() < self.__array[j].lower()):
                tmp.append(self.__array[i])
                i += 1
            else:
                tmp.append(self.__array[j])
                j += 1

        for step in range(0, right - left + 1):
            if self.__array[left + step].lower() != tmp[step].lower():
                self.__array[left + step] = tmp[step]

    def __merge_sort_nums_descending(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)

        self.__merge_sort_nums_descending(left, mid)
        self.__merge_sort_nums_descending(mid + 1, right)

        i = left
        j = mid + 1
        tmp = list()
        for step in range(0, right - left + 1):
            if j > right or (i < mid + 1 and self.__array[i] > self.__array[j]):
                tmp.append(self.__array[i])
                i += 1
            else:
                tmp.append(self.__array[j])
                j += 1

        for step in range(0, right - left + 1):
            if self.__array[left + step] != tmp[step]:
                self.__array[left + step] = tmp[step]

    def __merge_sort_strings_descending(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)

        self.__merge_sort_strings_descending(left, mid)
        self.__merge_sort_strings_descending(mid + 1, right)

        i = left
        j = mid + 1
        tmp = list()
        for step in range(0, right - left + 1):
            if j > right or (i < mid + 1 and self.__array[i].lower() > self.__array[j].lower()):
                tmp.append(self.__array[i])
                i += 1
            else:
                tmp.append(self.__array[j])
                j += 1

        for step in range(0, right - left + 1):
            if self.__array[left + step].lower() != tmp[step].lower():
                self.__array[left + step] = tmp[step]

    # main merge sort method
    # there are some checks for the right type of sort
    def merge_sort(self, left, right, asc, desc):
        self.__sort_time = time.time()
        if asc:
            if str(self.__array[0]).isalpha() or \
                    (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                     and "." not in str(self.__array[0])):
                self.__merge_sort_strings_ascending(left, right)
            else:
                self.__merge_sort_nums_ascending(left, right)
        elif desc:
            if str(self.__array[0]).isalpha() or \
                    (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                     and "." not in str(self.__array[0])):
                self.__merge_sort_strings_descending(left, right)
            else:
                self.__merge_sort_nums_descending(left, right)
        self.__sort_time = time.time() - self.__sort_time

    # main heap sort method
    # there are some checks for the right type of sort
    def heap_sort(self, asc, desc):
        self.__sort_time = time.time()
        # creating a heap from array
        for i in range(self.get_size() // 2 - 1, -1, -1):
            if asc:
                if str(self.__array[0]).isalpha() or\
                        (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                         and "." not in str(self.__array[0])):
                    self.__heap_sort_strings_ascending(i, self.get_size())

                else:
                    self.__heap_sort_nums_ascending(i, self.get_size())
            elif desc:
                if str(self.__array[0]).isalpha() or \
                        (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                         and "." not in str(self.__array[0])):
                    self.__heap_sort_strings_descending(i, self.get_size())
                else:
                    self.__heap_sort_nums_descending(i, self.get_size())

        # sifting heap to sort it
        if asc:
            for i in range(self.get_size() - 1, 0, -1):
                self.__array[i], self.__array[0] = self.__array[0], self.__array[i]
                if str(self.__array[0]).isalpha() or \
                        (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                         and "." not in str(self.__array[0])):
                    self.__heap_sort_strings_ascending(0, i)

                else:
                    self.__heap_sort_nums_ascending(0, i)
        elif desc:
            for i in range(self.get_size() - 1, -1, -1):
                self.__array[i], self.__array[0] = self.__array[0], self.__array[i]
                if str(self.__array[0]).isalpha() or \
                        (not str(self.__array[0]).isdigit() and "-" not in str(self.__array[0])
                         and "." not in str(self.__array[0])):
                    self.__heap_sort_strings_descending(0, i)
                else:
                    self.__heap_sort_nums_descending(0, i)
        self.__sort_time = time.time() - self.__sort_time

    # next 4 methods are sifting methods for heap sort
    def __heap_sort_strings_ascending(self, i, size):
        largest_child = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and self.__array[largest_child].lower() < self.__array[left_child].lower():
            largest_child = left_child

        if right_child < size and self.__array[largest_child].lower() < self.__array[right_child].lower():
            largest_child = right_child

        if largest_child != i:
            self.__array[i], self.__array[largest_child] = self.__array[largest_child], self.__array[i]

            self.__heap_sort_strings_ascending(largest_child, size)

    def __heap_sort_nums_ascending(self, i, size):
        largest_child = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and self.__array[largest_child] < self.__array[left_child]:
            largest_child = left_child

        if right_child < size and self.__array[largest_child] < self.__array[right_child]:
            largest_child = right_child

        if largest_child != i:
            self.__array[i], self.__array[largest_child] = self.__array[largest_child], self.__array[i]

            self.__heap_sort_nums_ascending(largest_child, size)

    def __heap_sort_strings_descending(self, i, size):
        smallest_child = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and self.__array[smallest_child].lower() > self.__array[left_child].lower():
            smallest_child = left_child

        if right_child < size and self.__array[smallest_child].lower() > self.__array[right_child].lower():
            smallest_child = right_child

        if smallest_child != i:
            self.__array[i], self.__array[smallest_child] = self.__array[smallest_child], self.__array[i]

            self.__heap_sort_strings_ascending(smallest_child, size)

    def __heap_sort_nums_descending(self, i, size):
        smallest_child = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and self.__array[smallest_child] > self.__array[left_child]:
            smallest_child = left_child

        if right_child < size and self.__array[smallest_child] > self.__array[right_child]:
            smallest_child = right_child

        if smallest_child != i:
            self.__array[i], self.__array[smallest_child] = self.__array[smallest_child], self.__array[i]

            self.__heap_sort_nums_ascending(smallest_child, size)

    # comparison between two sorts with same array using ascending and descending orders
    def compare(self):
        self.generate("0", "100", "100")
        array_copy = self.__array
        time_data = list()
        attempts = 10
        test_time = 0.
        for _ in range(0, attempts):
            self.merge_sort(0, self.get_size() - 1, True, False)
            test_time += self.get_sort_time()
            self.__array = array_copy
        time_data.append(test_time / attempts)
        test_time = 0.
        for _ in range(0, attempts):
            self.merge_sort(0, self.get_size() - 1, False, True)
            test_time += self.get_sort_time()
            self.__array = array_copy
        time_data.append(test_time / attempts)
        test_time = 0.
        for _ in range(0, attempts):
            self.heap_sort(True, False)
            test_time += self.get_sort_time()
            self.__array = array_copy
        time_data.append(test_time / attempts)
        test_time = 0.
        for _ in range(0, attempts):
            self.heap_sort(False, True)
            test_time += self.get_sort_time()
            self.__array = array_copy
        time_data.append(test_time / attempts)
        return time_data

    def get_string(self):
        return [str(i) for i in self.__array]

    def get_size(self):
        return len(self.__array)

    def get_array(self):
        return self.__array

    # converting file input in array
    def set_array(self, arr):
        self.__array = list()
        for i in arr:
            self.__array.append(str(i).strip("\n"))
        if self.check_array() == 'int':
            self.__array = [int(i) for i in self.__array]
        elif self.check_array() == 'float':
            self.__array = [float(i) for i in self.__array]

    # check array elements type
    def check_array(self):
        is_int = False
        is_float = False
        for i in self.__array:
            if i.isdigit() or i[0] == "-" and i[1:].isdigit():
                is_int = True
            elif not i.isalpha() and "." in i or \
                    not i.isalpha() and "." in i and i[0] == "-":
                is_float = True

        if is_int and is_float or is_float and not is_int:
            return 'float'
        elif is_int and not is_float:
            return 'int'
        else:
            return 'str'

    def get_sort_time(self):
        return self.__sort_time

    def is_empty(self):
        return self.get_size() == 0
