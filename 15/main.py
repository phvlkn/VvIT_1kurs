import face_recognition

# Загрузка изображений
known_image = face_recognition.load_image_file("ref.jpg")
unknown_image = face_recognition.load_image_file("cmp.jpg")

# Получение кодировок лиц
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Сравнение лиц
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

# Вывод результата
print("Совпадение найдено" if results[0] else "Совпадения нет.")