user = ""
while not user.strip():
    user = input("Tên tài khoản: ").strip()
    if not user:
        print("Tên tài khoản không được rỗng!")
video = input("Tiêu Đề Video: ").strip().title()
describe = ""
while not describe.strip():
    describe = input("Mô Tả :").strip()
    if not describe:
        print("Mô tả video không được rỗng!")
hashtag = input("HashTag(Cách nhau dấu ,): ").strip()
hashtags_list =hashtag.strip().split(",")
while True:
    print("Hệ Thống Quản Lý Nội Dung TikTok")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn Hóa Tên tài khoản")
    print("3. Kiếm Tra tính hợp lệ của hashtag")
    print("4. Tìm Kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát Chương Trình")
    choose = int(input("> Chọn Chức năng từ 1 - 5: "))

    match choose:
        case 1:
            describe_len = len(describe) # Số Lượng ký tự
            describe_words = len(describe.split()) # Số Lượng TỪ
            number_hashtag = len(hashtags_list)
            describe_lower = describe.lower()
            describe_upper = describe.upper()
            print("===========================================")
            print(f"Tên tài Khoản: {user} ")
            print(f"Tiêu đề: {video} ")
            print(f"Mô Tả: {describe} ")
            print(f"Độ dài mô tả: {describe_len}")
            print(f"Số từ mô tả trong video: {describe_words}")
            print(f"Hashtag: {hashtag}")
            print(f"Số Lượng Hashtag: {number_hashtag}")
            print(f"Mô Tả chữ thường: {describe_lower}")
            print(f"Mô tả chữ Hoa: {describe_upper}")
            print("===========================================")
        case 2:
            if not user.startswith("@"): # kiếm tra đầu mảng nếu ko có @ thì lấy @ + user
                re_user = "@" + user.lower()
            print(f"Tên gốc: {user}")
            print(f"Chuẩn Hóa: {re_user}")
        case 3:
            new_hashtag = input("Nhập hashtag để check: ").strip()
            if not new_hashtag:
                print("Không hợp lệ không đc rỗng!")
            elif not new_hashtag.startswith("#"):
                print("Phải bắt đầu bằng #")
            elif " " in new_hashtag:
                print("Không được chứa khoảng trắng")
            elif len(new_hashtag) < 2:
                print("ít nhất 2 kí tự bao gồm cả #")
            elif not all(tag.isalnum() or tag == "_" for tag in new_hashtag[1:]): # isalum : chỉ nhập chữ và kí tự cùng dùng for duyệt qua phần tự bắt đầu từ 1 bỏ qua #(0)
                print("không hợp lệ! chỉ được dùng chữ cái, chữ số hoặc dấu gạch dưới")
            else:
                print("Hợp Lệ ")
                hashtags_list.append(new_hashtag)
                print(f"Danh sách hiện tại: {hashtags_list}")
        case 4:
            word = input("Nhập từ khóa cần tìm: ").strip()
            replacement = input("Nhập từ thay thế: ")

            if word in describe:
                describe = describe.replace(word,replacement)
                print("Thay thế thành công!")
                print(f"Mới : {describe}")
            else: 
                print("không tìm thấy")
        case 5:
            print("Thoát Chương Trình!")
            break
        case _ :
            print("Lựa chọn không hợp lệ!")
