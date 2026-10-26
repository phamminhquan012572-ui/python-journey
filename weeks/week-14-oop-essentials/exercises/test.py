class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin, "mAh")
        print("Gia ban:", self.GiaBan, "VND")


# Tao 2 doi tuong theo de bai
DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

# Hien thi thong tin 2 dien thoai
DT01.thongtindienthoai()
print("--------------------")
DT02.thongtindienthoai()
