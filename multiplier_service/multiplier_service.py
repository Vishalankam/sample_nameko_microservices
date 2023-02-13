# from flask import request
from nameko.rpc import rpc, RpcProxy

class MultiplierService:
    name = 'multiplier_service'
    
    auth_service = RpcProxy('auth_service')
    
    @rpc
    def multiply(self, data, token):
        num1 = data.get('num_1')
        num2 = data.get('num_2')
        
        verified = self.auth_service.verify_user(token)
        
        if verified:
            return {"result": num1 * num2}, 200
        else:
            return "Unauthorized", 401
