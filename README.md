```md
# NanoGuard

NanoGuard is a lightweight file security scanner that identifies sensitive data such as API keys, tokens, passwords, and other secrets inside your local files. It operates entirely inside the user's home directory and uses strict confinement for safe and sandboxed execution.

## Installation

Install from the Snap Store:

```
sudo snap install nanoguard
```

## Usage

Scan any directory:

```
nanoguard <path>
```

Example:

```
nanoguard ~/Documents
```

## License

MIT
```
