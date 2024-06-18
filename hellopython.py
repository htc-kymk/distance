import math

# Noktaların Tanımlanması
points = [(2, 3), (5, 7), (1, 8), (4, 6), (7, 2)]

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafe
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# min
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")

