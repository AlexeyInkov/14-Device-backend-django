import {useToast} from "@chakra-ui/react";
import {useQuery} from "react-query";
import {fetchDevices} from "../serviсes/devices.js";

const useDevicesQuery = (state) => {
    const toast = useToast()

    return useQuery({
        queryFn: () => fetchDevices(state),
        queryKey: ['devices', state],
        staleTime: 1000 * 5,
        onError: (err) => {
            if (err instanceof Error) {
                toast({
                    status: 'error',
                    title: err.message,
                    position: 'top-right'
                })
            }
        }
    });
};

export {useDevicesQuery};