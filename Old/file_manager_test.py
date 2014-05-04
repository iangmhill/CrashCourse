from FileManager import FileManager

fm = FileManager()
catalog = fm.load_courses()

for course in catalog:
	print course.description