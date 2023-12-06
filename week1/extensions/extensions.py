def main():
    file_name = input("Enter file name: ").strip().lower()
    application_extensions = ["pdf", "txt", "zip"]
    image_extensions = ["gif", "jpg", "jpeg", "png"]

    chunked_file_name = file_name.split(".")

    if len(chunked_file_name) == 1:
        print("application/octet-stream")
        return 0

    extension = chunked_file_name[len(chunked_file_name) - 1]

    if (extension not in application_extensions and
            extension not in image_extensions):
        print("application/octet-stream")
    elif extension in application_extensions:
        print(f"text/plain") if extension == "txt" else print(f"application/{extension}")
    elif extension in image_extensions:
        extension = "jpeg" if extension == "jpg" else extension
        print(f"image/{extension}")


if __name__ == '__main__':
    main()
