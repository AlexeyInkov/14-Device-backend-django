import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {QueryClient, QueryClientProvider} from "react-query";
import {ChakraProvider} from "@chakra-ui/react";
import {ReactQueryDevtools} from "react-query/devtools";

const client = new QueryClient()

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <QueryClientProvider client={client}>
            <ChakraProvider>
                <App/>
                <ReactQueryDevtools initialIsOpen={false}/>
            </ChakraProvider>
        </QueryClientProvider>
    </StrictMode>,
)
