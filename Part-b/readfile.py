def file_op(file, mode, content=None):
    try:
        with open(file, mode) as f:
            if content is None:
                return f.read()
            f.write(content)
            return f"{'Appended to' if mode == 'a' else 'Written to'} '{file}' successfully."
    except (FileNotFoundError, Exception) as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    f = "C:\\Users\\Eshwar K\\OneDrive\\Desktop\\det.txt"
    print(f"Contents of '{f}':\n{file_op(f, 'r')}")
    print(file_op(f, 'a', input("Enter the content to append: ")))
