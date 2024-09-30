import '../styles/device.css';
import MenuFilter from "./menu_filter.jsx";
import {Spinner, Table, TableContainer, Tbody, Td, Th, Thead, Tr} from "@chakra-ui/react";
import {useDevicesQuery} from "../hooks/useDevicesQuery.js";
import {MouseOut, MouseOver} from "../utils/utils.js";
import {HEADERS_DEVICE} from "../config/constant.js";

function Devices({meteringUnitId}) {

    const {data, isLoading, isSuccess} = useDevicesQuery({meteringUnitId});

    if (isLoading) return (<Spinner
        thickness="4px"
        speed="0.65s"
        emptyColor="gray.200"
        color="blue.500"
        size="xl"
    />);

    const headerKeys = Object.keys(HEADERS_DEVICE)


    const deviceClick = (e) => {
        console.log(e.target.dataset.index);
    }

    return (<div className="window">
        <MenuFilter title={"верхнего поля"}/>
        {data[0]['id'] && (
        <TableContainer>
            <Table>
                <Thead>
                    <Tr>
                        {headerKeys.map((headerKey) => <Th key={headerKey}>{HEADERS_DEVICE[headerKey]}</Th>)}
                    </Tr>
                </Thead>
                <Tbody>
                    {isSuccess > 0 && data.map(dataItem => (
                        <Tr key={dataItem.id} data-index={dataItem.id} onMouseOver={MouseOver} onMouseOut={MouseOut}
                            onClick={deviceClick}>
                            {headerKeys.map((headerKey) => <Td key={headerKey} data-index={dataItem.verification}>{dataItem[headerKey]}</Td>)}
                        </Tr>
                    ))}
                </Tbody>
            </Table>
        </TableContainer>
            )}
    </div>);
}

export {Devices};