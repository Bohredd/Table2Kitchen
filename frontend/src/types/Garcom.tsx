import { Restaurante } from "./Restaurante";

export type Garcom = {
    id: number;
    nome: string;
    telefone: string;
    email: string;
    restaurante: Restaurante;
}