from service_config_db import GetmaintaskrouteALL


MainAPIRouteArray = {}

def initmainroute():
    cli_response = GetmaintaskrouteALL()

    global MainAPIRouteArray

    if cli_response['Code'] == '0':
        print cli_response['Message']
    else:
        TempRouteArray = cli_response['RowsArray']

        for TempObj in TempRouteArray:
            TempObj['service_func'] = TempObj['service_func'].encode('ascii')
            TempObj['service_url'] = TempObj['service_url'].encode('ascii')
            TempObj['type_baseurl'] = TempObj['type_baseurl'].encode('ascii')

        for TempObj in TempRouteArray:
            MainAPIRouteArray[str(TempObj['service_id'])] = TempObj

    # return TempMainAPIRouteArray