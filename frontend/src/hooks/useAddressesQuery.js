import {useToast} from "@chakra-ui/react";
import {useQuery} from "react-query";

import {fetchAddresses} from "../serviсes/address.js";

const useAddressesQuery = (state) => {
    const toast = useToast()

    return useQuery({
        queryFn: () => fetchAddresses(state),
        queryKey: ['addresses', state],
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

export {useAddressesQuery};