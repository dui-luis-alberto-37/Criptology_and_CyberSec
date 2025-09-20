class Encription:
      def __init__(self):
      
      def cesar_encrypt(self, data: str, key) -> str:
         # Simple encryption logic (for demonstration purposes)
         return ''.join(chr(ord(c) + len(key)) for c in data)
   
      def cesar_decrypt(self, data: str, key) -> str:
         # Simple decryption logic (for demonstration purposes)
         return ''.join(chr(ord(c) - len(key)) for c in data)
      
      def modular_linear_encrypt(self, data: str, )