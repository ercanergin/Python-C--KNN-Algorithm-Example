 import numpy as np
     import cv2
     from matplotlib import pyplot as plt
     
     img = cv2.imread('digits.png')
     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     
     # Şimdi görüntüyü 5000 hücrelere bölüyoruz, her 20x20 boyut
     cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
    
    # Artık train_data ve test_data hazırlıyoruz.
    x = np.array(cells)
    
    # Tren ve test verileri için etiketler oluşturun
    train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
    test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
    
    # KNN'yi başlatın, veriyi eğitin, ardından k = 1 için test verisi ile test edin
    k = np.arange(10)
    train_labels = np.repeat(k,250)[:,np.newaxis]
    test_labels = train_labels.copy()
    
    # Şimdi sınıflandırma doğruluğunu kontrol ediyoruz
    knn = cv2.KNearest()
    knn.train(train,train_labels)
    ret,result,neighbours,dist = knn.find_nearest(test,k=5)
    
    # Bunun için test_labels ile sonucu karşılaştırın ve hangilerinin yanlış olduğunu kontrol edin
    matches = result==test_labels
    correct = np.count_nonzero(matches)
    accuracy = correct*100.0/result.size
    print accuracy
