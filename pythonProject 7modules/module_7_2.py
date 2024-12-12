def custom_write(file_name, strings):

    strings_positions = {}
    if not strings:
        return strings_positions

    try:
        with open(file_name, 'w', encoding='utf-8') as f:  #Encoding is crucial!
            for i, line in enumerate(strings, 1):
                byte_offset = f.tell()
                f.write(line + '\n')
                strings_positions[(i, byte_offset)] = line
    except (IOError, OSError) as e:
        print(f"Error writing to file: {e}")
        return {}  # Return empty dict on error

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)