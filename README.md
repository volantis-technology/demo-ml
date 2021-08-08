## ML Model Demo
Service ML Model menggunakan Flask

### Kebutuhan
Scikit Learn, Numpy, Flask, Gunicorn, Docker, K8s.

### Menjalankan Aplikasi
1. Buat artefak model
```
python model.py
```
Nantinya akan muncul file dt.joblib

2. Menjalankan app.py
```
python app.py
```

3. Menjalankan menggunakan WSGI Gunicorn
```
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

4. Buka URL http://localhost:5000 untuk mencoba menggunakan UI atau menjalankan `request.py` menggunakan POST request


5. Kontainerisasi menggunakan docker dengan perintah
```
docker build -t volantis/demo-ml:latest .
```
Setelah image selesai dibuat, bisa dicoba untuk dijalankan dengan perintah
```
docker run -dp 8000:8000 volantis/demo-ml
```

6. Daftarkan ke kontainer repositori
```
docker push volantis/demo-ml
```

7. Terapkan pada cluster kubernetes
```
kubectl apply -f k8s/deploy.yaml
```
Setelah pod telah berjalan, bisa dicoba untuk meneruskan service port di cluster ke local kita dengan perintah
```
kubectl port-forward svc/volantis-demo-ml 8000:8000
```
