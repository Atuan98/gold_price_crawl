def get_area_name_code(area_name) -> str:
    if area_name in ['Hồ Chí Minh', 'TPHCM', 'HCM', 'SG', 'Tp.HCM']:
        area_name = 'HCM'
    if area_name in ['Hà Nội', 'HN', 'Hanoi', 'Ha Noi']:
        area_name = 'HN'
    if area_name in ['Đà Nẵng', 'Đà  Nẵng', 'Danang', 'ĐN', 'DN']:
        area_name = 'DN'
    if area_name in ['Huế', 'Hue', 'HUẾ', 'HUE']:
        area_name = 'HUE'
    if area_name in ['Bình Phước', 'Binh Phuoc', 'BP']:
        area_name = 'BP'
    if area_name in ['Biên Hòa', 'Bien Hoa', 'BH']:
        area_name = 'BH'
    if area_name in ['Miền Tây', 'Mien Tay', 'MT']:
        area_name = 'MT'
    if area_name in ['Quảng Ngãi', 'Quãng Ngãi','Quang Ngai', 'QN']:
        area_name = 'QUANGNGAI'
    if area_name in ['Long Xuyên', 'Long Xuyen', 'LX']:
        area_name = 'LX'
    if area_name in ['Bạc Liêu', 'Bac Lieu', 'BL']:
        area_name = 'BL'
    if area_name in ['Quy Nhơn', 'Quy Nhon']:
        area_name = 'QUYNHON'
    if area_name in ['Phan Rang', 'PP']:
        area_name = 'PR'
    if area_name in ['Hạ Long', 'Ha Long', 'HL']:
        area_name = 'HL'
    if area_name in ['Quảng Nam', 'Quang Nam']:
        area_name = 'QUANGNAM'
    if area_name in ['Nha Trang', 'NT']:
        area_name = 'NT'
    if area_name in ['Cần Thơ', 'Can Tho']:
        area_name = 'CT'
    if area_name in ['Cà Mau', 'Ca Mau', 'CM']:
        area_name = 'CM'
    if area_name in ['Giá vàng nữ trang', 'Gia vang nu trang', 'GVNT']:
        area_name = 'GVNT'
    return area_name


def get_type_gold_code(type_name) -> str:
    if type_name in ['SJC', 'Vàng SJC']:
        type_name = 'SJC'
    if type_name in ['Vàng SJC 1L - 10L']:
        type_name = 'SJC 1L-10L'
    if type_name in ['Vàng nhẫn SJC 99,99 1 chỉ, 2 chỉ, 5 chỉ']:
        type_name = 'VN SJC 125'
    if type_name in ['Vàng nhẫn SJC 99,99 0,5 chỉ']:
        type_name = 'VN SJC 9999 0.5'
    if type_name in ['Vàng nữ trang 99,99%']:
        type_name = 'VNT 9999'
    if type_name in ['Vàng nữ trang 99%']:
        type_name = 'VNT 99'
    if type_name in ['Vàng nữ trang 75%']:
        type_name = 'VNT 75'
    if type_name in ['Vàng nữ trang 58,3%']:
        type_name = 'VNT 583'
    if type_name in ['Vàng nữ trang 41,7%']:
        type_name = 'VNT 417'
    if type_name in ['Nhẫn PNJ (24K)']:
        type_name = 'NPNJ 24K'
    if type_name in ['Nữ trang 24K']:
        type_name = 'NT 24K'
    if type_name in ['Nữ trang 18K']:
        type_name = 'NT 18K'
    if type_name in ['Nữ trang 14K']:
        type_name = 'NT 14K'
    if type_name in ['Nữ trang 10K']:
        type_name = 'NT 10K'
    if type_name in ['Nguyên liêu 9999 - HN', 'Nguyên liêu 9999 ', 'Nguyên liêu 9999']:
        type_name = 'NL9999-HN'
    if type_name in ['Nguyên liêu 999 - HN', 'Nguyên liêu 999 ', 'Nguyên liêu 999']:
        type_name = 'NL999-HN'
    if type_name in ['AVPL/SJC Cần Thơ']:
        type_name = 'AVPL/SJC CT'

    return type_name