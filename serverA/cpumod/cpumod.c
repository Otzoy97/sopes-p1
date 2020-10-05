#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/mm.h>
#include <linux/swap.h>

#include <linux/cpumask.h>
#include <linux/kernel_stat.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sergio Otzoy");
MODULE_DESCRIPTION("Modulo para obtener uso de CPU");
MODULE_VERSION("0.01");
	
static int my_proc_show(struct seq_file *m, void *v) {
	unsigned long cpu = *((unsigned long*) cpu_possible_mask->bits);
	unsigned long total = 0;
	struct kernel_cpustat *info = NULL;

	int idx = 0;
	while(cpu) {
		info = (struct kernel_cpustat*) ((unsigned long) __per_cpu_offset[idx]+(unsigned long)&kernel_cpustat);

		total += info->cpustat[CPUTIME_NICE];
		total += info->cpustat[CPUTIME_SYSTEM];
		total += info->cpustat[CPUTIME_SOFTIRQ];
		total += info->cpustat[CPUTIME_IRQ];
		total += info->cpustat[CPUTIME_IDLE];
		total += info->cpustat[CPUTIME_IOWAIT];
		total += info->cpustat[CPUTIME_STEAL];
		total += info->cpustat[CPUTIME_GUEST];
		total += info->cpustat[CPUTIME_GUEST_NICE];
		
		cpu /= 2;
	}

	seq_printf(m, "%lu", total);
	return 0;
}

static ssize_t my_proc_write(struct file *file, const char __user *buffer, size_t count, loff_t *f_pos) {
	return 0;
}

static int my_proc_open(struct inode *inode, struct file *file)
{
	return single_open(file, my_proc_show, NULL);
}

static struct file_operations my_fops = {
	.owner = THIS_MODULE,
	.open = my_proc_open,
	.release = single_release,
	.read = seq_read,
	.llseek = seq_lseek,
	.write = my_proc_write
};

static int __init cpumod_init(void) {
	struct proc_dir_entry *entry = proc_create("cpumod", 0777, NULL, &my_fops);
	if (!entry){
		return -1;
	} else {
		printk(KERN_INFO "Cpumod init\n");
	}
	return 0;
}

static void __exit cpumod_exit(void) {
	remove_proc_entry("cpumod", NULL);
	printk(KERN_INFO "Final\n");
} 

module_init(cpumod_init);
module_exit(cpumod_exit);