class RealService:
    def request(self, data):
        print(f"[RealService] Đang xử lý: {data}")

class ServiceProxy:
    def __init__(self):
        self.real_service = None

    def request(self, user, data):
        # Kiểm tra quyền
        if user != "admin":
            print("[Proxy] Người dùng không có quyền truy cập!")
            return
        
        if not self.real_service:
            print("[Proxy] Khởi tạo RealService...")
            self.real_service = RealService()
        
        print("[Proxy] Chuyển request cho RealService...")
        self.real_service.request(data)

if __name__ == "__main__":
    proxy = ServiceProxy()
    

    proxy.request("guest", "Hello")  
    print("---")

    proxy.request("admin", "Hello")  
