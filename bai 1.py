cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===============================================")
    print("         SHOPEE CART MANAGEMENT SYSTEM         ")
    print("===============================================")
    print("1. Xem chi tiết giỏ hàng và tính tổng tiền     ")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng       ")
    print("3. Cập nhật số lượng của một sản phẩm          ")
    print("4. Xóa sản phẩm khỏi giỏ hàng                  ")
    print("5. Thoát chương trình                          ")
    print("===============================================")

    choice = int(input("Mời bạn chọn chức năng (1-5): "))
    match choice:
        case 1:

            total = 0
            total_quantity = 0

            print("--- CHI TIẾT GIỎ HÀNG ---")

            print(f"{'STT':<5} | {'Mã SP':<8} | {'Tên sản phẩm':<25} | {'SL':<3} | {'Đơn giá':<10} | {'Thành tiền':<12}")
            print("------------------------------------------------------------------------")

            for i, item in enumerate(cart_items, start=1):

                product_id = item[0]
                product_name = item[1]
                quantity = item[2]
                price = item[3]

                subtotal = quantity * price

                total += subtotal
                total_quantity += quantity

                print(f"{i:<5} | {product_id:<8} | {product_name:<25} | {quantity:<3} | {price:<10} | {subtotal:<12}")

            print(f"Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
            print(f"TỔNG TIỀN THANH TOÁN: {total:,} đ")

        case 2:

            updated = False

            product_id = input("Nhập mã sản phẩm: ")

            for item in cart_items:

                if product_id == item[0]:

                    print(f"Đang cộng dồn số lượng sản phẩm {product_id}")

                    quantity = int(input("Nhập số lượng: "))

                    item[2] += quantity

                    updated = True

                    print(f"Cộng dồn sản phẩm {product_id} thành công")

                    break

            else:

                product_name = input("Nhập tên sản phẩm: ")

                quantity = int(input("Nhập số lượng: "))

                price = int(input("Nhập đơn giá: "))

            if not updated:

                cart_items.append([product_id, product_name, quantity, price])

                print("Thêm sản phẩm thành công!")

        case 3:

            product_id = input("Nhập mã sản phẩm muốn thay đổi: ")

            for item in cart_items:

                if product_id == item[0]:

                    new_quantity = int(input("Nhập số lượng mới cần thay đổi: "))

                    item[2] = new_quantity

                    print("Cập nhật số lượng thành công!")

                    break

            else:
                print(f"Không tìm thấy mã {product_id}")

        case 4:


            product_id = input("Nhập mã sản phẩm muốn xóa: ")

            for item in cart_items:

                if product_id == item[0]:

                    cart_items.remove(item)

                    print(f"Đã xóa sản phẩm có mã {product_id} khỏi giỏ hàng.")

                    break

            else:
                print(f"Không tìm thấy mã {product_id} trong giỏ hàng.")

        case 5:

            print("Thoát chương trình!")

            break