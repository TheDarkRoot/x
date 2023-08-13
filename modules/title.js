function console_title(x) {
    if (process.platform == 'win32') {
        process.title = x + " / SmsBomb v1.0.0 (Alpha)";
    } else {
        process.stdout.write('\x1b]2;' + x + " / SmsBomb v1.0.0 (Alpha)" + '\x1b\x5c');
    }
}

module.exports = console_title;