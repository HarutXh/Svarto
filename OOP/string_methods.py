class MyString:
    def __init__(self, s):
        self.__s = s

    def capitalize(self):
        first_char = self.__s[0]
        if ord(first_char) in range(65, 91):
            capitalize_str = self.__s
        else:
            capitalize_str = chr(ord(self.__s[0]) - 32) + self.__s[1:]
        return capitalize_str

    def casefold(self):
        result = ""
        for char in self.__s:
            if ord(char) >= 65 and ord(char) <= 90:
                casefold_char = chr(ord(char) + 32)
                result += casefold_char
            else:
                casefold_char = char
                result += casefold_char
        return result

    def center(self, width, fillchar=" "):
        if len(self.__s) >= width:
            return self.__s

        num_fill_chars = width - len(self.__s)
        num_left_fill_chars = num_fill_chars // 2
        num_right_fill_chars = num_fill_chars - num_left_fill_chars

        left_fill = fillchar * num_left_fill_chars
        right_fill = fillchar * num_right_fill_chars

        return left_fill + self.__s + right_fill

    def count(self, sub, start=0, end=-1):
        count = 0

        if end == -1:
            end = len(self.__s)

        for i in range(start, end - len(sub) + 1):
            if self.__s[i : i + len(sub)] == sub:
                count += 1

        return count

    def encode(self):
        encoded_string = ""
        for i in range(len(self.__s)):
            encoded_char = str(ord(self.__s[i]))
            if i == len(self.__s) - 1:
                encoded_string += encoded_char
            else:
                encoded_string += encoded_char + " "
        return encoded_string

    def endswith(self, suffix):
        return self.__s[-len(suffix) :] == suffix

    def expandtabs(self, tabsize=8):
        result = ""
        column = 0
        for char in self.__s:
            if char == "\t":
                spaces = tabsize - (column % tabsize)
                result += " " * spaces
                column += spaces
            else:
                result += char
                column += 1
        return result

    def format(self, *args):
        result = ""
        arg_index = 0
        i = 0
        n = len(self.__s)

        while i < n:
            char = self.__s[i]
            if char == "{":
                arg_str = ""
                i += 1
                while i < n and "0" <= self.__s[i] <= "9":
                    arg_str += self.__s[i]
                    i += 1
                if i < n and self.__s[i] == "}":
                    arg_index = int(arg_str)
                    result += str(args[arg_index])
                else:
                    raise ValueError("Invalid format string")
            elif char == "}":
                raise ValueError("Invalid format string")
            else:
                result += char
            i += 1
        return result

    def format_map(self, mapping):
        result = ""
        i = 0
        n = len(self.__s)

        while i < n:
            char = self.__s[i]
            if char == "{":
                arg_name = ""
                i += 1
                while i < n and self.__s[i] != "}":
                    arg_name += self.__s[i]
                    i += 1
                if i >= n or self.__s[i] != "}":
                    raise ValueError("Invalid format string")
                if arg_name in mapping:
                    result += str(mapping[arg_name])
                else:
                    raise KeyError("Key not found: {}".format(arg_name))
            else:
                result += char
            i += 1

        return result

    def index(self, sub, start=0, end=-1):
        if end == -1:
            end = len(self.__s)

        if start < 0:
            start += len(self.__s)
        if end < 0:
            end += len(self.__s)

        i = start
        while i < end - len(sub) + 1:
            if self.__s[i : i + len(sub)] == sub:
                return i
            i += 1

        raise ValueError("substring not found")

    def isalnum(self):
        for char in self.__s:
            if not ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9"):
                return False
        return True

    def isalpha(self):
        for char in self.__s:
            if not ("a" <= char <= "z" or "A" <= char <= "Z"):
                return False
        return True

    def isascii(self):
        for char in self.__s:
            if ord(char) < 128:
                return False
        return True

    def isdecimal(self):
        for char in self.__s:
            if not ("0" <= char <= "9"):
                return False
        return True

    def isdigit(self):
        for char in self.__s:
            if not ("0" <= char <= "9"):
                return False
        return True

    def isidentifier(self):
        if not self.__s:
            return False
        if not (
            "a" <= self.__s[0] <= "z" or "A" <= self.__s[0] <= "Z" or self.__s[0] == "_"
        ):
            return False
        for char in self.__s[1:]:
            if not (
                "a" <= char <= "z"
                or "A" <= char <= "Z"
                or char == "_"
                or "0" <= char <= "9"
            ):
                return False
        return True

    def islower(self):
        for char in self.__s:
            if "A" <= char <= "Z":
                return False
        return True

    def isnumeric(self):
        for char in self.__s:
            if not ("0" <= char <= "9"):
                return False
        return True

    def isprintable(self):
        for char in self.__s:
            if ord(char) < 32 or ord(char) > 126:
                return False
        return True

    def isspace(self):
        for char in self.__s:
            if not (
                char == " "
                or char == "\t"
                or char == "\n"
                or char == "\r"
                or char == "\f"
                or char == "\v"
            ):
                return False
        return True

    def istitle(self):
        prev_char = " "
        for char in self.__s:
            if char >= "A" and char <= "Z":
                if prev_char == " " or prev_char == "":
                    prev_char = char
                else:
                    return False
            prev_char = char
        return True

    def isupper(self):
        for char in self.__s:
            if "a" <= char <= "z":
                return False
        return True

    def join(self, iterable):
        result = ""
        for i in range(len(iterable)):
            result += str(iterable[i])
            if i != len(iterable) - 1:
                result += self.__s
        return result

    def ljust(self, width, fillchar=" "):
        if width <= len(self.__s):
            return self.__s
        else:
            fill_len = width - len(self.__s)
            fill_str = fillchar * fill_len
            return self.__s + fill_str

    def lower(self):
        new_str = ""
        for char in self.__s:
            if "A" <= char <= "Z":
                new_str += chr(ord(char) + 32)
            else:
                new_str += char
        return new_str

    def lstrip(self, chars=" \t\n\r\f\v"):
        new_str = self.__s
        while len(new_str) > 0 and new_str[0] in chars:
            new_str = new_str[1:]
        return new_str

    def maketrans(from_chars, to_chars):
        if len(from_chars) != len(to_chars):
            raise ValueError("from_chars and to_chars must have the same length")
        table = {}
        for i in range(len(from_chars)):
            table[ord(from_chars[i])] = to_chars[i]
        return table

    def translate(s, table):
        result = ""
        for char in s:
            if ord(char) in table:
                result += table[ord(char)]
            else:
                result += char
        return result

    def partition(self, sep):
        sep_len = len(sep)

        for i in range(len(self.__s)):
            if self.__s[i : i + sep_len] == sep:
                before = self.__s[:i]
                after = self.__s[i + sep_len :]
                return before, sep, after

        return self.__s, "", ""

    def replace(self, old, new):
        result = ""
        i = 0

        while i < len(self.__s):
            if self.__s[i : i + len(old)] == old:
                result += new
                i += len(old)
            else:
                result += self.__s[i]
                i += 1

        return result

    def rfind(self, substring, start=None, end=None):
        if start is None:
            start = len(self.__s) - 1
        if end is None:
            end = -1
        for i in range(start, end, -1):
            if self.__s[i : i + len(substring)] == substring:
                return i
        return -1

    def rindex(self, substring):
        length = len(self.__s)
        sub_length = len(substring)
        for i in range(length - sub_length, -1, -1):
            if self.__s[i : i + sub_length] == substring:
                return i
        raise ValueError("substring not found")

    def rjust(self, width, fillchar=" "):
        if len(self.__s) >= width:
            return self.__s
        else:
            padding = (width - len(self.__s)) * fillchar
            return padding + self.__s

    def rpartition(self, separator):
        for i in range(len(self.__s) - 1, -1, -1):
            if self.__s[i : i + len(separator)] == separator:
                return (self.__s[:i], separator, self.__s[i + len(separator) :])
        return ("", "", self.__s)

    def rsplit(self, separator, maxsplit=-1):
        parts = []
        count = 0
        i = len(self.__s) - len(separator)
        while i >= 0 and count != maxsplit:
            if self.__s[i : i + len(separator)] == separator:
                parts.append(string[i + len(separator) :])
                self.__s = self.__s[:i]
                count += 1
            i -= 1
        parts.append(self.__s)
        parts.reverse()
        return parts[:maxsplit] if maxsplit > 0 else parts

    def rstrip(self, characters=None):
        if characters is None:
            characters = " \t\n\r\v\f"  # default whitespace characters
        i = len(self.__s) - 1
        while i >= 0 and self.__s[i] in characters:
            i -= 1
        return self.__s[: i + 1]

    def split(self, separator=None, maxsplit=-1):
        result = []
        start = 0
        count = 0
        i = 0
        while i < len(self.__s):
            if maxsplit >= 0 and count >= maxsplit:
                break
            if self.__s[i] == separator:
                result.append(self.__s[start:i])
                start = i + 1
                count += 1
            i += 1
        result.append(self.__s[start:])
        return result

    def splitlines(self, keepends=False):
        lines = self.__s.split("\n")
        if keepends:
            return [line + "\n" for line in lines[:-1]] + [lines[-1]]
        else:
            return lines

    def startswith(self, prefix):
        return self.__s[: len(prefix)] == prefix

    def strip(self):
        start = 0
        end = len(self.__s) - 1

        while start <= end and self.__s[start] in (" ", "\t", "\n"):
            start += 1

        while end >= start and self.__s[end] in (" ", "\t", "\n"):
            end -= 1

        return self.__s[start : end + 1]

    def swapcase(self):
        result = ""
        for char in self.__s:
            if "A" <= char <= "Z":
                result += chr(ord(char) + 32)
            elif "a" <= char <= "z":
                result += chr(ord(char) - 32)
            else:
                result += char
        return result

    def title(self):
        result = ""
        capitalize_next = True
        for c in self.__s:
            if capitalize_next and "a" <= c <= "z":
                result += chr(ord(c) - 32)
                capitalize_next = False
            elif not capitalize_next and "A" <= c <= "Z":
                result += chr(ord(c) + 32)
            else:
                result += c
                if c == " " or c == "\t" or c == "\n":
                    capitalize_next = True
        return result

    def upper(self):
        result = ""
        for c in self.__s:
            if "a" <= c <= "z":
                result += chr(ord(c) - 32)
            else:
                result += c
        return result

    def zfill(self, width):
        if len(self.__s) >= width:
            return s
        else:
            zeros_needed = width - len(self.__s)
            return "0" * zeros_needed + self.__s


if __name__ == "__main__":
    my_string = MyString("hello, world!")
    mystring = MyString("h\te\nl\tl\to, world!")
    mystr = MyString("My name is {0}, I'm {1} years old, I'm live {2}")
    mystr1 = MyString("My name is {name}, I'm {age} years old, I'm live {city}")
    mapping = {"name": "Alice", "age": 30, "city": "New York"}
    my_s = MyString("abc123")
    my_strg = MyString("abcde123")
    my_string1 = MyString("Привет")
    mys = MyString("123456")
    string = MyString("s23str_")
    title = MyString("My Name Is Eminem")
    str_upper = MyString("HARUT")
    string_join = MyString(" ")
    lst = ["apple", "banana", "orange"]
    str_lstrip = MyString("      Hello, World!      ")
    s = "hello world"
    table = MyString.maketrans("aeiou", "12345")
    s = MyString.translate(s, table)
    st = "hello world"
    text = "First line\nSecond line\r\nThird line"
    num = "101"
    print(my_string.capitalize())
    print(my_string.casefold())
    print(my_string.center(20))
    print(my_string.count("o"))
    print(my_string.encode())
    print(my_string.endswith("d!"))
    print(mystring.expandtabs(2))
    print(mystr.format("Harut", 21, "Vanadzor"))
    print(mystr1.format_map(mapping))
    print(my_string.index("world!"))
    print(my_s.isalnum())
    print(my_strg.isalpha())
    print(my_string1.isascii())
    print(my_s.isdecimal())
    print(mys.isdigit())
    print(string.isidentifier())
    print(my_strg.islower())
    print(mys.isnumeric())
    print(mys.isprintable())
    print(mys.isspace())
    print(title.istitle())
    print(str_upper.isupper())
    print(string_join.join(lst))
    print(my_s.ljust(15, "-"))
    print(str_upper.lower())
    print(str_lstrip.lstrip())
    print(s)
    print(st.partition(" "))
    print(my_string.replace("o", "!"))
    print(my_string.rfind("l"))
    print(my_string.rindex("l"))
    print(my_string.rjust(15))
    print(st.rpartition(" "))
    print(st.rsplit(","))
    print(str_lstrip.rstrip())
    print(st.split())
    print(text.splitlines())
    print(my_string.startswith("hello"))
    print(text.strip())
    print(my_string.swapcase())
    print(my_string.title())
    print(my_string.upper())
    print(num.zfill(5))
