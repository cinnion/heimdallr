<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Schema\Grammars\Grammar;
use Illuminate\Support\Facades\Schema;

Grammar::macro('typeCidr', function() {
    return 'cidr';
});

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('filterlog', function (Blueprint $table) {
            $table->id();
            $table->timestampTz('timestamp');
            $table->string('hostname', 32);
            $table->integer('rule_num');
            $table->string('sub_rule', 32);
            $table->string('anchor', 64);
            $table->string('tracker', 64);
            $table->string('interface', 16);
            $table->string('reason', 16);
            $table->string('action', 16);
            $table->string('direction', 4);
            $table->smallInteger('ip_version');
            $table->string('tos', 8)->nullable();
            $table->string('ecn', 8)->nullable();
            $table->smallInteger('ttl')->nullable();
            $table->integer('pkt_id')->nullable();
            $table->integer('pkt_offset')->nullable();
            $table->string('flags', 32)->nullable();
            $table->string('pkt_class', 8)->nullable();
            $table->string('flow_label', 8)->nullable();
            $table->integer('hop_limit')->nullable();
            $table->integer('proto_id');
            $table->string('protocol', 16);
            $table->integer('pkt_length');
            $table->ipAddress('source_ip');
            $table->ipAddress('dest_ip');
            $table->jsonb('rest');

            $table->index('dest_ip');
            $table->index('source_ip');
            $table->index('timestamp');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('filterlog');
    }
};
