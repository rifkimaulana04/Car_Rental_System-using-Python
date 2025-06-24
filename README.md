# 🚗 Car Rental System — Full-Stack Web Project

A modern, responsive, and feature-rich web application for renting cars. This system enables users to browse available cars, book or return rentals, and provides an admin panel for full CRUD (Create, Read, Update, Delete) control over the fleet.

---

## 🎯 Features

### 👥 User Features
- View available cars with images and descriptions
- Real-time status (Available / Rented)
- Book a car with one click
- Return a rented car
- SwiperJS 3D car showcase slider
- Flip card hover animations
- Dark mode toggle
- Mobile-first responsive design

---

### 🛠️ Admin Panel
- Add new cars with image URL
- Edit car details (name, status, image)
- Delete/remove cars from the system
- View total, rented, and available cars (dashboard cards)

---
### 💎 UI/UX Enhancements
- Glassmorphism and neumorphism elements
- Toast alerts and smooth animations
- Newsletter signup (static)
- Social media footer links
- Stylish navigation with hover effects
- Modern fonts and clean layout

---

## 🛠️ Tech Stack

| Category        | Tech / Library |
|----------------|----------------|
| Backend        | Python, Flask  |
| Frontend       | HTML5, CSS3, Bootstrap 5, JavaScript |
| Templating     | Jinja2         |
| Animations     | SwiperJS, CSS Transforms |
| Data Storage   | `cars.txt` file (CSV format) |
| Deployment (optional) | Render, Railway, or Localhost |

---

## 📂 Folder Structure

car-rental/
├── app.py
├── cars.txt
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── cars.html
│ ├── rent.html
│ ├── return.html
│ └── admin.html
├── static/
│ ├── style.css
│ ├── icons/
│ └── images/
└── README.md


---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- Flask installed (`pip install flask`)

### Setup Steps

```bash
git clone https://github.com/rutujakale111/Car_Rental_System-using-Python
cd car-rental-system
pip install flask
python app.py
```
The app will run at ```http://localhost:5000```
