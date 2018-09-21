request = function()
    wrk.body = "{ \"client_id\":\"tahitian\",\"unit_id\":\"wukong_F3QUFi0MxwTBOQkQ7209\",\"detail\": {\"imp\": 1,\"clk\": -1 }}"
    wrk.headers["Content-Type"] = "application/json"
    return wrk.format('POST', '/track/detail') 
end