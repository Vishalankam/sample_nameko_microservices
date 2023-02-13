# from flask import request
from nameko.rpc import rpc, RpcProxy

class AuthService:
    name = 'auth_service' 
    #defining the name of the service
    #by using this name we can call any rpc function in this service

    @rpc
    def login(self, data):
        username = data.get('user_name')
        password = data.get('password')
        #verify the  username and password if its correct then return the authtoken
        #we can use the jwt to encode the data and generate the authtoken
        if username == 'username1' and password == 'password1':
            return "random_auth_token", 200
        else:
            return 'Not authenticated', 401
    
    @rpc  
    #defining it as the RPC function so that it can be called from other services 
    def verify_user(self, token):   
        #verify the data from the auth_token, if its correct then return the True
        #we can use the jwt to decode the auth_token
        if token == 'random_auth_token':
            return True
        else:
            return False
        