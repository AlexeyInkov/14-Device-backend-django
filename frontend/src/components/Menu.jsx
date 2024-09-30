import "../styles/menu.css"
import {useMenuQuery} from "../hooks/useMenuQuery.js";
import {Accordion, AccordionButton, AccordionItem, AccordionPanel, Box, Spinner} from "@chakra-ui/react";

const Menu = ({setTsoId, setCustomerId, setMeteringUnitId}) => {

    const {data, isLoading, isSuccess} = useMenuQuery();
    const tsoClick = (e) => {
        setTsoId(e.target.dataset.index);
        setCustomerId(null);
        setMeteringUnitId(null);
    }
    const customerClick = (e) => {
        setCustomerId(e.target.dataset.index);
        setMeteringUnitId(null);
    }

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

    return (
        <div className="window">
            <Accordion allowToggle id="accordion-basic">
                {isSuccess && data.map((tso) => (
                        <AccordionItem key={tso.id}>
                            <h3>
                                <AccordionButton>
                                    <Box as='span' flex='1' textAlign='left' data-index={tso.id} onClick={tsoClick}>
                                        {tso.name}
                                    </Box>
                                </AccordionButton>
                            </h3>
                            <AccordionPanel pb={4}>
                                <Accordion id="accordion-wrap">
                                    {tso.customers.map((customer) => (
                                            <h3 key={customer.id}>
                                                <AccordionButton>
                                                    <Box as='span' flex='1' textAlign='left' data-index={customer.id}
                                                         onClick={customerClick}>
                                                        {customer.name}
                                                    </Box>
                                                </AccordionButton>
                                            </h3>

                                        )
                                    )}
                                </Accordion>
                            </AccordionPanel>
                        </AccordionItem>
                    )
                )}
            </Accordion>
        </div>
    );
}

export {Menu};

