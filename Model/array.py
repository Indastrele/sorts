import random
import time
from PySide6.QtWidgets import QMessageBox


class Array:
    def __init__(self):
        self.__array = list()
        self.__sort_time = float()

    def __generator(self, left_border, right_border, size):
        for i in range(0, size):
            self.__array.append(random.randint(left_border, right_border))

    def __float_generator(self, left_border, right_border, size):
        for i in range(0, size):
            self.__array.append(round(random.uniform(left_border, right_border), 3))

    def generate(self, left, right, size_input):
        error = QMessageBox()
        self.__array = list()
        if len(left) == 0 or len(right) == 0 or len(size_input) == 0:
            error.warning(error, "Сообщение об ошибке", "Отсутствует ввод данных",
                          QMessageBox.StandardButton.Close)
            return
        if size_input.isdigit():
            size = int(size_input)
        else:
            error.warning(error, "Сообщение об ошибке", "Размер должен быть целым числом",
                          QMessageBox.StandardButton.Close)
            return

        if left.isalpha() and right.isalpha():
            if len(left) > 1 or len(right) > 1:
                error.setText("Input is string, not char.")
                error.setWindowTitle("Error")
                error.exec()
                return

            left = ord(left)
            right = ord(right)

            self.__generator(left, right, size)
            tmp_array = list()
            for i in self.__array:
                tmp_array.append(chr(i))

            self.__array = tmp_array
        elif left.isdigit() and right.isdigit():
            left = int(left)
            right = int(right)

            self.__generator(left, right, size)
        elif not left.isalpha() and not right.isalpha():
            left = float(left)
            right = float(right)

            self.__float_generator(left, right, size)
        else:
            error.warning(error, "Сообщение об ошибке", "Данные должны быть одного типа", QMessageBox.
                          StandardButton.Close)

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

    def merge_sort(self, left, right, asc, desc):
        self.__sort_time = time.time()
        if asc:
            if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                self.__merge_sort_strings_ascending(left, right)
            else:
                self.__merge_sort_nums_ascending(left, right)
        elif desc:
            if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                self.__merge_sort_strings_descending(left, right)
            else:
                self.__merge_sort_nums_descending(left, right)
        self.__sort_time = time.time() - self.__sort_time

    def heap_sort(self, asc, desc):
        self.__sort_time = time.time()
        for i in range(self.get_size() // 2 - 1, -1, -1):
            if asc:
                if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                    self.__heap_sort_strings_ascending(i, self.get_size())

                else:
                    self.__heap_sort_nums_ascending(i, self.get_size())
            elif desc:
                if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                    self.__heap_sort_strings_descending(i, self.get_size())
                else:
                    self.__heap_sort_nums_descending(i, self.get_size())

        if asc:
            for i in range(self.get_size() - 1, 0, -1):
                self.__array[i], self.__array[0] = self.__array[0], self.__array[i]
                if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                    self.__heap_sort_strings_ascending(0, i)

                else:
                    self.__heap_sort_nums_ascending(0, i)
        elif desc:
            for i in range(self.get_size() - 1, -1, -1):
                self.__array[i], self.__array[0] = self.__array[0], self.__array[i]
                if str(self.__array[0]).isalpha() or not str(self.__array[0]).isdigit():
                    self.__heap_sort_strings_descending(0, i)
                else:
                    self.__heap_sort_nums_descending(0, i)
        self.__sort_time = time.time() - self.__sort_time

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

    def get_string(self):
        return [str(i) for i in self.__array]

    def get_size(self):
        return len(self.__array)

    def get_array(self):
        return self.__array

    def set_array(self, arr):
        self.__array = list()
        for i in arr:
            self.__array.append(i.strip("\n"))
        if self.__array[0].isdigit():
            self.__array = [int(i) for i in self.__array]
        elif not self.__array[0].isalpha():
            self.__array = [float(i) for i in self.__array]

    def get_sort_time(self):
        return self.__sort_time
