result = '{"results":[{"statement_id":0,"series":[{"name":"upstreams","tags":{"name":"auth_adm_int"},"columns":["time","percentile"],"values":[["2024-10-08T06:25:00Z",2]]},{"name":"upstreams","tags":{"name":"int-cdi-upstream"},"columns":["time","percentile"],"values":[["2024-10-21T18:25:00Z",5]]},{"name":"upstreams","tags":{"name":"int-ehd-upstream"},"columns":["time","percentile"],"values":[["2024-09-23T06:50:00Z",4]]},{"name":"upstreams","tags":{"name":"int-eip-fin-info-upstream"},"columns":["time","percentile"],"values":[["2024-10-09T13:45:00Z",181]]},{"name":"upstreams","tags":{"name":"int-eip-rpd-upstream"},"columns":["time","percentile"],"values":[["2024-09-24T13:15:00Z",189]]},{"name":"upstreams","tags":{"name":"int-eip-virtual-payments-upstream"},"columns":["time","percentile"],"values":[["2024-10-15T09:00:00Z",2]]},{"name":"upstreams","tags":{"name":"int-epk-instance-upstream"},"columns":["time","percentile"],"values":[["2024-10-16T05:25:00Z",6]]},{"name":"upstreams","tags":{"name":"int-epk-sdk-upstream"},"columns":["time","percentile"],"values":[["2024-10-01T10:55:00Z",2]]},{"name":"upstreams","tags":{"name":"int-epk-upstream"},"columns":["time","percentile"],"values":[["2024-10-16T05:20:00Z",2]]},{"name":"upstreams","tags":{"name":"int-lp-upstream"},"columns":["time","percentile"],"values":[["2024-10-08T10:10:00Z",4]]},{"name":"upstreams","tags":{"name":"int-muz-upstream"},"columns":["time","percentile"],"values":[["2024-10-15T13:10:00Z",1]]},{"name":"upstreams","tags":{"name":"int-orpon-upstream"},"columns":["time","percentile"],"values":[["2024-09-26T07:15:00Z",1]]},{"name":"upstreams","tags":{"name":"int-otrs-upstream"},"columns":["time","percentile"],"values":[["2024-10-07T13:00:00Z",1]]},{"name":"upstreams","tags":{"name":"int-pi-upstream"},"columns":["time","percentile"],"values":[["2024-09-26T07:15:00Z",2]]},{"name":"upstreams","tags":{"name":"int-rms-upstream"},"columns":["time","percentile"],"values":[["2024-09-25T11:10:00Z",3]]},{"name":"upstreams","tags":{"name":"int-wfm-sibir-upstream"},"columns":["time","percentile"],"values":[["2024-10-18T06:10:00Z",1]]},{"name":"upstreams","tags":{"name":"integration_fedsol-rt_v1"},"columns":["time","percentile"],"values":[["2024-10-07T08:25:00Z",3]]}]}]}'

#print(type(rr))
rr = result.split(',')
print(rr)
print("len rr = ", len(rr))

def analiz_requests(rr,count,upstreams):
    index_value = 6 #kagdie 6 index - value
    for i in range(0,len(rr)):
        if "values" in rr[i]: #dostaem value
#            print(rr[i])
    #        index = rr.index(rr[i])
#            print("index = ", index_value)
#            print(rr[index_value])
            buff = rr[index_value]
            buff = buff.replace("]","")
            buff = buff.replace("}","")
#            print(buff)
            index_value = index_value + 6
            count.append(int(buff))
        if "tags" in rr[i]: #dostaem upstream-name
    #        print(rr[i])
            buff = rr[i]
            buff = buff.split('"')
    #        print(buff[5])
            upstreams.append(buff[5])
    #        print(rr[3])


upstreams = []
count_arr = []

analiz_requests(rr, count_arr, upstreams)

print(upstreams)
print(count_arr)
# for i in range(0,len(upstreams)):
#     print(upstreams[i], " = ",count_arr[i], "\n")

result = '{"results":[{"statement_id":0}]}'
result2 = '{"results":[{"statement_id":0,"series":[{"name":"upstreams","tags":{"name":"int-lp-upstream"},"columns":["time","sum"],"values":[["2024-10-24T06:45:54.31947196Z",2]]},{"name":"upstreams","tags":{"name":"int-otrs-upstream"},"columns":["time","sum"],"values":[["2024-10-24T06:45:54.31947196Z",2]]},{"name":"upstreams","tags":{"name":"int-rms-upstream"},"columns":["time","sum"],"values":[["2024-10-24T06:45:54.31947196Z",2]]}]}]}'

rr = result2.split(',')

print(rr)
if isinstance(rr,str):
    print(type(rr))
else:
    print(len(rr))
    upstreams2 = []
    count_arr2 = []

    analiz_requests(rr, count_arr2, upstreams2)
    print(upstreams2)
    print(count_arr2)

    for i in range(0,len(upstreams2)):
        if upstreams2[i] in upstreams:
            if count_arr2[i] < count_arr[i]:
                print("alert!!!!")
