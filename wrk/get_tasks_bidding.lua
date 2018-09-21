request = function()
    wrk.body = 'client_id=0&task_type=1'
    return wrk.format('GET', '/get_tasks/bidding?client_id=0&task_type=0&quantity=10') 
end