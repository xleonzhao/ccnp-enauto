import codecs

# file="/home/xzhao/Downloads/Certifications__2CiscoDev__ENAUTO.apkg"
file="/tmp/apg/713"

def detect_encoding(file):
    with open(file, "rb") as f:
        encoding = codecs.detect_encoding(f.read())
        return encoding['encoding']

def detect_encoding2(file):
    with open(file, "rb") as f:
        data = f.read()

        possible_encodings = ["utf-8", "latin-1", "iso-8859-1"]
        for enc in possible_encodings:
            try:
                data.decode(enc)
            except UnicodeDecodeError as e:
                print(f"Failed to decode with {enc}, error is {e}")
                continue
            else:
                return enc

def convert_file(file, old_enc, new_enc):
    with open(file, "rb") as f:
        data = f.read()

    new_file = f'{file}.new.txt'
    new_data = data.decode(old_enc)

    with open(new_file, "w", encoding=new_enc) as f:
        f.write(new_data)

enc = detect_encoding2(file)
print(enc)
if enc != "utf-8":  
    convert_file(file, enc, "utf-8")
    print(f"Converted {file} from {enc} to utf-8")
