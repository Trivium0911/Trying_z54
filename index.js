const TASK_3_URL = '/task/3';
const TASK_4_URL = '/task/4';


async function api_call(url, arg) {
    const resp = await fetch(
        url, {
            body: arg,
            method: 'POST',
        });

    if (resp.status !== 200) {
        return null;
    }

    const payload = await resp.json();

    return payload;
}


async function getNumber() {
    const payload = await api_call(TASK_4_URL, 'stop');
    return payload.data.n;
}


async function addNumber(number) {
    const payload = await api_call(TASK_4_URL, number);
    return payload.data.n;
}


async function greet(name) {
    const payload = await api_call(TASK_3_URL, name);
    return payload.data.greeting;
}


async function setUpTask3() {
    let input = document.querySelector("#task3 input");
    let span = document.querySelector("#task3 span");

    input.addEventListener("input", async function (event) {
        const name = input.value;
        const greeting = await greet(name);
        span.textContent = greeting;
    });
}


async function setUpTask4() {
    let label = document.querySelector("#task4 label");
    let input = document.querySelector("#task4 input");
    let button = document.querySelector("#task4 button");

    const ping = async function () {
        const number = await getNumber();
        label.textContent = `Накопление: ${number}`;
    }

    //setInterval(ping, 5000);
    //await ping();

    button.addEventListener("click", async function (event) {
        if (input.value === "stop") {
            await ping();
            return;
        };
        let value = Number.parseInt(input.value || '0');
        if (value == 'NaN') {
            value = 0;
        }
        input.value = 0;
        await addNumber(value);
        await ping();
    });
}


async function setUp() {
    await setUpTask3();
    await setUpTask4();
}

document.addEventListener("DOMContentLoaded", setUp);