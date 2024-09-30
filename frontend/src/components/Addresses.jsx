import '../styles/address.css';
import MenuFilter from "./menu_filter.jsx";
import {Spinner, Table, TableContainer, Tbody, Td, Th, Thead, Tr} from "@chakra-ui/react";
import {useAddressesQuery} from "../hooks/useAddressesQuery.js";
import {MouseOut, MouseOver} from "../utils/utils.js";
import {HEADERS_ADDRESS} from "../config/constant.js";

function Addresses({tsoId, customerId, setMeteringUnitId}) {

    const {data, isLoading, isSuccess} = useAddressesQuery({tsoId, customerId});

    if (isLoading)
        return (
            <Spinner
                thickness="4px"
                speed="0.65s"
                emptyColor="gray.200"
                color="blue.500"
                size="xl"
            />
        );

    const headerKeys = Object.keys(HEADERS_ADDRESS)


    const meteringUnitClick = (e) => {
        setMeteringUnitId(e.target.dataset.index);
}

    return (
        <div className="window">
            <MenuFilter title={"верхнего поля"}/>
            <TableContainer>
            <Table>
                <Thead>
                    <Tr>
                        {headerKeys.map((headerKey) => <Th key={headerKey}>{HEADERS_ADDRESS[headerKey]}</Th>)}
                    </Tr>

                </Thead>
                <Tbody>
                    {isSuccess && data.map(dataItem => (
                        <Tr key={dataItem.id} onMouseOver={MouseOver} onMouseOut={MouseOut} onClick={meteringUnitClick}>
                            {headerKeys.map((headerKey) => <Td key={headerKey} data-index={dataItem.id}>{dataItem[headerKey]}</Td>)}
                        </Tr>
                    ))}
                </Tbody>
            </Table>
            </TableContainer>
        </div>
    );
}

export {Addresses};