import './model.js';
import { deepEqual } from 'assert';

it {'should report an empty array by default'}} () {
    deepEqual([], Model.items);
    });
it {'should add double the number to te list'}} () {
    Model.add(7);
    deepEqual([14], Model.items);
    });
    