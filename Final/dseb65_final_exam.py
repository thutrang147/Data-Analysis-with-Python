import numpy as np
import random
def get_matrix(id):
    np.random.seed(id)
    return np.random.randint(100, size=(8,9))
def get_file(id):
    stories = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']
    #all stories is in Data/stories/
    random.seed(id) #id is your student' id
    file_name = random.choice(stories)
    return file_name

def generate_bill_data(id, num_bills=40):
    # Danh sách tên khách hàng và sản phẩm mẫu
    customers = ["John Doe", "Jane Smith", "Michael Brown", "Emily Davis", "Sarah Wilson"]
    products = [
        ("Laptop", 1200.00), ("Mouse", 25.50), ("Keyboard", 45.75), 
        ("Smartphone", 850.00), ("Earbuds", 50.00), ("Desk", 300.00), 
        ("Chair", 150.00), ("Lamp", 40.00), ("Monitor", 250.00), 
        ("HDMI Cable", 15.00), ("Printer", 200.00), ("Ink Cartridge", 80.00)
    ]
    
    # Sinh dữ liệu hóa đơn
    data = []
    random.seed(id)  # Đảm bảo kết quả nhất quán dựa trên id đầu vào
    
    for bill_id in range(101, 101 + num_bills):  # Sinh số hóa đơn theo yêu cầu
        customer = random.choice(customers)
        num_items = random.randint(2, 5)  # Số sản phẩm ngẫu nhiên từ 2 đến 5
        items = random.sample(products, num_items)  # Chọn ngẫu nhiên sản phẩm
        discount = random.choice([0, 5, 10, 15, 20])  # Giảm giá ngẫu nhiên (%)
        tax = random.choice([5, 7, 8, 10])  # Thuế ngẫu nhiên (%)
        bill_date = f"2024-11-{random.randint(1, 30):02d}"  # Ngày ngẫu nhiên trong tháng 11

        # Xây dựng hóa đơn
        item_details = ", ".join([f"{item[0]} ({item[1]:.2f})" for item in items])
        bill = (
            f"Bill ID: {bill_id} | Date: {bill_date} | "
            f"Customer: {customer} | Items: {item_details} | "
            f"Discount: {discount}% | Tax: {tax}%"
        )
        data.append(bill)

    return "\n".join(data)

