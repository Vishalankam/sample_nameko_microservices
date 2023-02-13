from nameko.rpc import rpc, RpcProxy

class AdderService:
    name = 'adder_service'
    auth_service = RpcProxy('auth_service')
    #RpcProxy used to inter-communicate between the nameko services
    
    @rpc
    def add(self, data, token):
        num1 = data.get('num_1')
        num2 = data.get('num_2')
        
        verified = self.auth_service.verify_user(token)
        #calling the rpc function of auth_service
        
        if verified:
            addition = num1 + num2
            return {"result": addition}, 200
        else:
            return "Unauthorized", 401
