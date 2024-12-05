# Araç Sayma Programı (Kütüphane Kullanılmadan)
# Yazar: Assistant
# Tarih: 2023

# PPM görüntülerini okuyup yazmak, görüntü işleme ve araç sayma işlemleri için fonksiyonlar içerir.

# PPM formatındaki görüntüyü okuyan fonksiyon
def read_ppm(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Yorum satırlarını ve boş satırları atla
    lines = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    
    # Başlığı oku ve doğrula
    assert lines[0] == 'P3', 'PPM formatı değil!'
    dimensions = lines[1].split()
    width, height = int(dimensions[0]), int(dimensions[1])
    max_color = int(lines[2])
    
    # Piksel verilerini oku
    pixels = []
    pixel_data = ' '.join(lines[3:]).split()
    for i in range(0, len(pixel_data), 3):
        r = int(pixel_data[i])
        g = int(pixel_data[i+1])
        b = int(pixel_data[i+2])
        pixels.append((r, g, b))
    
    return width, height, pixels

# PPM formatında görüntüyü kaydeden fonksiyon
def write_ppm(filename, width, height, image):
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write('255\n')
        for pix in image:
            f.write(f'{pix[0]} {pix[1]} {pix[2]} ')
            # Satır sonu için isteğe bağlı olarak ekleyebilirsiniz
            # f.write('\n')

# İki görüntü arasındaki farkı hesaplayan fonksiyon
def frame_difference(image1, image2, threshold):
    diff_image = []
    for pix1, pix2 in zip(image1, image2):
        # Piksel farkını hesapla
        diff = sum([abs(c1 - c2) for c1, c2 in zip(pix1, pix2)])
        if diff > threshold:
            diff_image.append((255, 255, 255))  # Hareketli piksel (beyaz)
        else:
            diff_image.append((0, 0, 0))  # Sabit piksel (siyah)
    return diff_image

# Bağlantılı bileşen analizi yapan fonksiyon
def connected_components(binary_image, width, height):
    labels = [0] * len(binary_image)
    label = 1
    equivalences = {}
    
    for y in range(height):
        for x in range(width):
            idx = y * width + x
            if binary_image[idx] == (255, 255, 255):
                neighbors = []
                if x > 0 and labels[idx - 1] > 0:
                    neighbors.append(labels[idx - 1])
                if y > 0 and labels[idx - width] > 0:
                    neighbors.append(labels[idx - width])
                
                if not neighbors:
                    labels[idx] = label
                    label += 1
                else:
                    min_label = min(neighbors)
                    labels[idx] = min_label
                    for neighbor_label in neighbors:
                        if neighbor_label != min_label:
                            equivalences[neighbor_label] = min_label
    
    # Eşdeğerlikleri düzeltme
    for idx in range(len(labels)):
        lbl = labels[idx]
        while lbl in equivalences:
            lbl = equivalences[lbl]
        labels[idx] = lbl
    
    return labels

# Nesnelerin konumlarını bulan fonksiyon
def get_object_positions(labels, width, height):
    objects = {}
    for y in range(height):
        for x in range(width):
            idx = y * width + x
            label = labels[idx]
            if label > 0:
                if label in objects:
                    objects[label]['pixels'].append((x, y))
                else:
                    objects[label] = {'pixels': [(x, y)]}
    # Nesnelerin merkezlerini hesaplayalım
    for obj in objects.values():
        xs = [p[0] for p in obj['pixels']]
        ys = [p[1] for p in obj['pixels']]
        obj['center'] = (sum(xs) / len(xs), sum(ys) / len(ys))
    return objects

# Nesne takip ve sayma için sınıf
class ObjectTracker:
    def __init__(self, line_y):
        self.objects = {}
        self.next_id = 1
        self.line_y = line_y
        self.count = 0
    
    def update(self, detected_objects):
        updated_objects = {}
        for obj_id, obj_data in self.objects.items():
            obj_data['updated'] = False
        
        for obj in detected_objects.values():
            center = obj['center']
            assigned = False
            for oid, data in self.objects.items():
                prev_center = data['center']
                # Nesneleri eşleştirme kriteri (yakınlık)
                if abs(center[0] - prev_center[0]) < 20 and abs(center[1] - prev_center[1]) < 20:
                    updated_objects[oid] = {'center': center}
                    assigned = True
                    # Çizgi geçiş kontrolü
                    if (prev_center[1] < self.line_y and center[1] >= self.line_y):
                        self.count += 1
                    break
            if not assigned:
                # Yeni nesne
                updated_objects[self.next_id] = {'center': center}
                self.next_id += 1
        self.objects = updated_objects

# Görüntü üzerine çizgi çizen fonksiyon
def draw_line(image, width, height, line_y):
    y = int(line_y)
    for x in range(width):
        idx = y * width + x
        if idx < len(image):
            image[idx] = (255, 0, 0)  # Mavi renkli çizgi

# Nesnelerin merkezlerini görüntüye çizen fonksiyon
def draw_objects(image, width, objects):
    for obj in objects.values():
        x, y = int(obj['center'][0]), int(obj['center'][1])
        idx = y * width + x
        if 0 <= idx < len(image):
            image[idx] = (0, 255, 0)  # Yeşil renkli nokta

# Ana fonksiyon
def main():
    line_y = 100  # Çizginin y koordinatı (görüntünün üst kısmından itibaren piksel cinsinden)
    tracker = ObjectTracker(line_y)
    prev_width, prev_height, prev_image = read_ppm('frame1.ppm')
    
    frame_number = 2
    while True:
        try:
            filename = f'frame{frame_number}.ppm'
            width, height, image = read_ppm(filename)
            
            # Fark görüntüsünü hesapla
            diff_image = frame_difference(prev_image, image, threshold=30)
            
            # Hareketli nesneleri bul
            labels = connected_components(diff_image, width, height)
            detected_objects = get_object_positions(labels, width, height)
            
            # Nesneleri güncelle
            tracker.update(detected_objects)
            
            # Görüntüyü çiz
            draw_line(image, width, height, line_y)
            draw_objects(image, width, detected_objects)
            
            # Sonucu kaydet
            output_filename = f'output{frame_number}.ppm'
            write_ppm(output_filename, width, height, image)
            
            # Bir sonraki kareye geç
            prev_image = image
            frame_number += 1
        except FileNotFoundError:
            # Daha fazla kare yoksa döngüden çık
            break
    
    print(f'Toplam araç sayısı: {tracker.count}')

# Programı çalıştır
if __name__ == '__main__':
    main()
