# Verileri kaydetmek
    2 np.savez('knn_data.npz',train=train, train_labels=train_labels)
    3 
    4 # Şimdi veriyi yükle
    5 with np.load('knn_data.npz') as data:
    6     print data.files
    7     train = data['train']
    8     train_labels = data['train_labels']
