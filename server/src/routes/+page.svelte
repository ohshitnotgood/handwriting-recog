<script lang="ts">
    import { onMount } from "svelte";

    let width = 600;
    let height = 600;
    let color = "#333";
    let background = "#fff";

    let canvas: HTMLCanvasElement;
    let context: CanvasRenderingContext2D;
    let isDrawing: boolean;
    let start: any;

    let t: number, l: number;

    onMount(() => {
        context = canvas.getContext("2d")!;
        context.fillStyle = "#fff";
        context.fillRect(0, 0, width, height);

        handleSize();
    });

    $: if (context) {
        context.strokeStyle = color;
    }

    const handleStart = ({ offsetX: x, offsetY: y }) => {
        if (color === background) {
            context.clearRect(0, 0, width, height);
        } else {
            isDrawing = true;
            start = { x, y };
        }
    };

    const handleEnd = () => {
        isDrawing = false;
    };

    const handleMove = ({ offsetX: x1, offsetY: y1 }) => {
        if (!isDrawing) return;

        const { x, y } = start;
        context.beginPath();

        context.lineWidth = 30
        context.lineCap = "round"

        context.moveTo(x, y);

        context.lineTo(x1, y1);
        context.closePath();
        context.stroke();

        start = { x: x1, y: y1 };
    };

    const handleSize = () => {
        const { top, left } = canvas.getBoundingClientRect();
        t = top;
        l = left;
    };

    function onSubmit() {
        const imageData = context.getImageData(0, 0, width, height).data
        console.log(imageData)
    }

    function clearCanvas() {
        context.clearRect(0, 0, width, height);
    }
</script>

<svelte:window on:resize={handleSize} />

<div class="w-screen h-screen grid place-content-center text-center">
    <canvas
        {width}
        {height}
        bind:this={canvas}
        on:mousedown={handleStart}
        on:touchstart={(e) => {
            const { clientX, clientY } = e.touches[0];
            handleStart({
                offsetX: clientX - l,
                offsetY: clientY - t,
            });
        }}
        on:mouseup={handleEnd}
        on:touchend={handleEnd}
        on:mouseleave={handleEnd}
        on:mousemove={handleMove}
        on:touchmove={(e) => {
            const { clientX, clientY } = e.touches[0];
            handleMove({
                offsetX: clientX - l,
                offsetY: clientY - t,
            });
        }}
        class="border border-gray-300 rounded-md mx-auto my-4 cursor-crosshair"
    />

    <div class="flex space-x-1 mx-auto">
        <button class="button-13" on:click={onSubmit}> Detect </button>
        <button class="button-13" on:click={clearCanvas}> Clear </button>
    </div>
</div>

<style>
    .button-13 {
        background-color: #fff;
        border: 1px solid #d5d9d9;
        border-radius: 8px;
        box-shadow: rgba(213, 217, 217, 0.5) 0 2px 5px 0;
        box-sizing: border-box;
        color: #0f1111;
        cursor: pointer;
        display: inline-block;
        font-family: "Amazon Ember", sans-serif;
        font-size: 13px;
        line-height: 29px;
        padding: 0 10px 0 11px;
        position: relative;
        text-align: center;
        text-decoration: none;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: middle;
        width: 100px;
    }

    .button-13:hover {
        background-color: #f7fafa;
    }

    .button-13:focus {
        border-color: #008296;
        box-shadow: rgba(213, 217, 217, 0.5) 0 2px 5px 0;
        outline: 0;
    }
</style>
