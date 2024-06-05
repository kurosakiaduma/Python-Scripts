from re import match


def decode(message_file):
    encoded = {}
    try:
        with open(message_file, "r", encoding="utf-8") as f:
            file_lines = f.readlines()

            # Extract the number and its respective text
            for line in file_lines:
                key = match('\d+', line).group()
                text = match('\w+\s+\w+', line).group().split()[-1]
                encoded[key] = text

            # Extract the numbers from the encoded dict
            nums = [int(i) for i in list(encoded.keys())]
            nums = sorted(nums)
            step = 1
            pyramid = []

            # Arrange them in a pyramid
            while len(nums) > 0:
                pyramid.append(nums[0:step])
                nums = nums[step:]
                step += 1
        code = []
        for p in pyramid:
            code.append(p[-1])

        string = ""
        for c in code:
            string += encoded.get(str(c)) + " "

        print(string)
    except FileNotFoundError:
        print("The file does not exist!")
    finally:
        f.close()

    try:
        return string
    except UnboundLocalError:
        return None

if __name__ == "__main__":
    decode("coding_qual_input.txt")
