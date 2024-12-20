import { StatusPedido } from "./StatusPedido";
import { Produto } from "./Produto";
import { Mesa } from "./Mesa";
import { Garcom } from "./Garcom";

export type Pedido = {
    id: number;
    garcom: Garcom;
    produtos: Produto[];
    mesa: Mesa;
    status: StatusPedido;
    horario_pedido: string;
};