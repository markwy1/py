points = [{'x': 2, 'y': 3},{'x': 4, 'y': 1}, {'x': 6, 'y': 2}]
points.sort(key=lambda a: a['y'], reverse=True)
print(points)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10)]  # last item is not follewed a , is ok


print(student_tuples)

a = sorted(student_tuples, key=lambda i: i[2]) # sorted return values
print(a)

student_tuples.sort(key=lambda i: i[2])
print(student_tuples)




