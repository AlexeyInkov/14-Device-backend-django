import {useToast} from "@chakra-ui/react";
import {useQuery} from "react-query";
import {fetchMenu} from "../serviсes/menu.js";

const useMenuQuery = () => {
    const toast = useToast()

    return useQuery({
        queryFn: fetchMenu,
        queryKey: ['menu'],
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

export {useMenuQuery};