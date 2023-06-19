<script>

    String.prototype.isValidMessage = function() {
        return this.trim() !== "";
    };

    import "../app.css"
</script>

<slot />