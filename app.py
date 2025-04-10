from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
CARS_FILE = 'cars.txt'

# Helper to load all cars
def load_cars():
    cars = []
    with open('cars.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                car_id, name, status, image = parts
                cars.append({
                    'car_id': car_id,
                    'name': name,
                    'status': status,
                    'image': image
                })
    return cars


# Helper to save cars
def save_cars(cars):
    with open('cars.txt', 'w') as file:
        for car in cars:
            line = f"{car['car_id']},{car['name']},{car['status']},{car['image']}\n"
            file.write(line)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cars')
def view_cars():
    cars = load_cars()
    return render_template('cars.html', cars=cars)

@app.route('/rent', methods=['GET', 'POST'])
def rent_car():
    cars = load_cars()
    if request.method == 'POST':
        car_id = request.form['car_id']
        for car in cars:
            if car['car_id'] == car_id and car['status'] == 'Available':
                car['status'] = 'Rented'
                save_cars(cars)
                break
        return redirect(url_for('view_cars'))
    return render_template('rent.html', cars=cars)

@app.route('/return', methods=['GET', 'POST'])
def return_car():
    cars = load_cars()
    if request.method == 'POST':
        car_id = request.form['car_id']
        for car in cars:
            if car['car_id'] == car_id and car['status'].lower() == 'rented':
                car['status'] = 'Available'
                save_cars(cars)
                break
        return redirect(url_for('view_cars'))
    return render_template('return.html', cars=cars)

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    cars = load_cars()
    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            car_id = request.form['car_id']
            name = request.form['name']
            cars.append({'car_id': car_id, 'name': name, 'status': 'Available'})
        elif action == 'remove':
            car_id = request.form['car_id']
            cars = [car for car in cars if car['car_id'] != car_id]
        save_cars(cars)
        return redirect(url_for('admin_panel'))
    return render_template('admin.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
